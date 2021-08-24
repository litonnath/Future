import  scrapy
from scrapy_splash import SplashRequest
from scrapy_splash import SplashFormRequest
from scrapy.http import FormRequest
from scrapy.utils.response import  open_in_browser
class splash(scrapy.Spider):
    name='t1'
    start_urls=[
        'https://search.ipindia.gov.in/DesignApplicationStatus/'
    ]


    def parse1(self,response):

        #sending data to form using splash
        return SplashFormRequest.from_response(response,url='https://search.ipindia.gov.in/DesignApplicationStatus/',formdata={'APPLICATION_NUMBER':'222230','CaptchaText':'hijdjs'},clickdata={'name':'submit'},callback=self.parse)


        #Below for without splash
        # return FormRequest.from_response(response,formdata={'APPLICATION_NUMBER':'222230','CaptchaText':'hijdjs'},clickdata={'name':'submit'},callback=self.parse)



   #After login ,Data Fetech below script
    def parse(self, response):
        open_in_browser(response)
        yield {
            'Application Number: ': response.xpath('/html/body/div[2]/div/div/div/section/div/div[2]/div[2]/label').get(),
            'Cbr Number:': response.xpath('/html/body/div[2]/div/div/div/section/div/div[3]/div[2]/label').get(),
            'Cbr Date': response.xpath('/html/body/div[2]/div/div/div/section/div/div[4]/div[1]/label').get(),
            'Applicant Name': response.xpath('/html/body/div[2]/div/div/div/section/div/div[5]/div[2]/label').get(),
            'Application Status:': response.xpath('/html/body/div[2]/div/div/div/section/div/div[7]/div[2]/label').get()
        }
