class HomeController < ApplicationController
before_action :authenticate_user!

require 'open-uri'
require 'nokogiri'

def index
  @title = Array.new
  @content = Array.new
  @calendar = Array.new
  @set = Array.new
  
    doc = Nokogiri::HTML(URI.open("https://job.incruit.com/calendar/calendar.asp").read)
    crawl_data1 = doc.css('body > div:first-child > div#PageFrame > div#PageContent > table > tr:nth-child(3) > td > div#divCalendar > table > tbody > tr:nth-child(3) > td')
    crawl_data1.each do |t|
      title = t.css('div:nth-child(odd)')
      title = title.css('a').text.split(" ")
      @title << title

      content = t.css('div:nth-child(even)')
      content = content.map{|element| element["jobtitle"]}.compact
      @content << content

      calendar = t.css('div:nth-child(even)')
      calendar = calendar.map{|element| element["invitedt"]}.compact
      @calendar << calendar

      for num in 0..title.length()
        @set.push([title[num], content[num], calendar[num]])

        end
      end
  end
end
