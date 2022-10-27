namespace :crawling do
  task company_collect: :environment do
    require 'open-uri'
    require 'net/http'

    doc = Nokogiri::HTML(URI.open("https://job.incruit.com/calendar/calendar.asp").read)
    crawl_data1 = doc.css('body > div:first-child > div#PageFrame > div#PageContent > table > tr:nth-child(3) > td > div#divCalendar > table > tbody > tr:nth-child(3)
                 > td')
    crawl_data2 = doc.css('body > div:first-child > div#PageFrame > div#PageContent > table > tr:nth-child(3) > td > div#divCalendar > table > tbody > tr:nth-child(3)
    > td > div:nth-child(even) > div')
    crawl_data1.each do |t|

      title = t.css('div:nth-child(odd)')
      title = title.css('a').text.split(" ")
      puts "모집중인 회사 : #{title}"

      #content = t.css('div:nth-child(even)')
      #content = content.map{|element| element["jobtitle"]}.compact
      #puts "회사 모집 주요 내용 : #{content}"

      #calendar = t.css('div:nth-child(even)')
      #calendar = calendar.map{|element| element["invitedt"]}.compact
      #puts "모집중인 모집 기간 : #{calendar}"


      #testing2 = calendar('[invitedt]')['invitedt']
      #puts testing2

      #testing = t.at_css('[invitedt]')['invitedt']
     # puts testing


      #puts "회사: #{title}, #{calendar}"

    crawl_data2.each do |t|
      #title = t.css('div').text
      #calendar = t['invitedt']
      #calendar2 = calendar.at[:'invitedt']
      #puts "날짜:#{calendar}"
    end
    end
  end
end