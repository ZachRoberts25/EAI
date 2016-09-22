require 'httparty'
def website_crawler(number_of_websites)
  return "Please enter a positive number greater than 1" if number_of_websites <= 0
  if number_of_websites < 25
    response = HTTParty.get('http://www.alexa.com/topsites')
    return parse(response)[0..number_of_websites - 1]
  else
    big_array = []
    number_of_pages = (number_of_websites / 25.0).ceil
    number_of_pages.times do |i|
      response = HTTParty.get("http://www.alexa.com/topsites/global;#{i}")
      big_array << parse(response)
    end
    big_array.flatten![0..number_of_websites - 1]
  end
end
  def parse(response)
    body = response.body
    array = body.scan(/\/siteinfo\/.*\">/)
    array.each {|i| i.slice!(0..9)}
    array.each {|i| i.slice!(/\">/)}
  end

p website_crawler(30)
