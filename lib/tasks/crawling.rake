namespace :crawling do
  task company_collect: :environment do
    require 'open-uri'
    require 'net/http'

    doc = Nokogiri::HTML(URI.open("http://job.incruit.com/entry///").read)
    crawl_data = doc.css('body > div#incruit_wrap > div#incruit_container > div#incruit_contents > div.shb_body > div.section_layout > div.verti_btm45 > div.enrty_header > div#divCalendarList > div.enrty_listbox')
    crawl_data.each do |t|

      start = t.css('dl').text
      company = t.css('dl > dd > p').text


      puts "#{company} : #{state}"
      end
    end
end