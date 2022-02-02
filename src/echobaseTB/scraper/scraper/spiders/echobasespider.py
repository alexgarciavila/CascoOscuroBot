import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser

class echobaseTB(scrapy.Spider):
    name = "echobaseTB"
    start_urls = [
        'https://echobase.app/login',
    ]
    login = {'echoBase_allyCode': '336544232', 'echoBase_guildId': '731123'}
    def parse(self, response):
        # login
        return FormRequest.from_response(response,
                                         formdata={
                                             'allyCode':'336544232'
                                                          },
                                         callback=self.after_login)

    def after_login(self, response):
        if 'Ally Code is invalid' in response.text:
            self.logger.error("Código de aliado incorrecto")
        else:
            self.logger.info("Código de aliado correcto")
            self.logger.info("Empezamos el scraping")
            return scrapy.Request(url='https://echobase.app/platoonAssigner',
                                  cookies=self.login,
                                  callback=self.pick_phase)

    def pick_phase(self, response):
        print("#########################################")
        print("##    SELECCIONAMOS LA BT Y LA FASE    ##")
        print("#########################################")

        from scrapy.shell import inspect_response
        inspect_response(response, self)

        # GEONOSIS LUMINOSA FASE 1
        return scrapy.Request(url='https://echobase.app//platoonAssigner?battle=RepublicOffensive&phase=1',
                              cookies={'echoBase_allyCode': '336544232', 'echoBase_guildId': '731123'},
                              callback=self.preview_pelotones)
    def preview_pelotones(self, response):
        print("#################################")
        print("##    PREVIEW LOS PELOTONES    ##")
        print("#################################")

        guild_name = response.xpath('//span[@id="navGuildName"]/text()').getall()

        print(guild_name)

        open_in_browser(response)
        #prueba = response.xpath('//div[@class="my-3"]//h5/span/text()[normalize-space()]').getall()
        #print(prueba)
