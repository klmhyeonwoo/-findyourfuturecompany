require 'open-uri'
require 'nokogiri'

doc = Nokogiri::HTML(open("https://www.naver.com"))

puts doc