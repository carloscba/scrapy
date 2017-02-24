import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

class Pasos(scrapy.Spider):
    name = "pasos"

    def start_requests(self):
        url = 'https://serpegen.gna.gob.ar/subfron/GNA_ListadoPasos.asp'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        pasosData = []

        pasos = Selector(response=response).xpath('//table[@id="listado"]//tr').extract()

        for paso in pasos:

            td = Selector(text=paso.encode("utf-8")).xpath('//tr/td/text()').extract()
            estado = Selector(text=paso.encode("utf-8")).xpath('//tr/td/a/text()').extract()

            if(len(td)) > 0:
                pasosData.append({
                    'nombre' : td[0].encode("utf-8"),
                    'provincia' : td[1].encode("utf-8"),
                    'pais' : td[2].encode("utf-8"),
                    'estado' : estado[0].encode("utf-8")
                })

        yield{
            'data' : pasosData
        } 