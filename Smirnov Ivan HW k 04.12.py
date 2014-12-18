# -*- coding: utf-8 -*-

from lxml import html, etree
import urllib2
import re

def read_url(url):
    page = urllib2.urlopen(url)
    charset = page.headers.getparam('charset')
    return page.read().decode(charset)

class Teachers(object):
    def __init__(self, surname, name, middlename, phone, address, email, job):
        self.surname = surname
        self.name = name
        self.middlename = middlename
        self.phone = phone
        self.address = address
        self.mail = email
        self.job = job
    @staticmethod
    def data(text):
        k = -1
        page = etree.XML(text, etree.HTMLParser())
        persons = page.xpath(".//div[@class='emp-text']")
        for each in persons:
            fio = each.xpath("./div/a")[0].text.split()
            if len(fio) == 2:
                fio.append('')
            address = each.xpath("./div/p[@class='addr']")
            if len(address) > 0:
                address = address[0].text.strip("\'\"")[7:]
            else:
                address = ''
            number = each.xpath("./div/p[@class='tel']")
            if len(number) > 0:
                number = number[0].text.strip("\'\"")[9:]
            else:
                number = ''
            mail = each.xpath("./div/p[@class='email']")
            if len(mail) > 0:
                f = re.sub('\'','',text,flags = re.U)
                f = re.sub('\+','',f,flags = re.U)
                f = re.sub('<wbr/>','',f,flags = re.U)
                email = re.findall("document\.write\((.*?)\)",f,flags = re.U)
                k += 1
            job = each.xpath("./div/p[@class='details']")[0].text.strip("\'\"")
            yield Teachers(fio[0], fio[1], fio[2], number, address, email[k],job)



page = read_url('http://www.hse.ru/org/persons/letter.html?ltr=%D0%AF')
people = Teachers.data(page)
for person in people:
    print person.surname, person.name, person.middlename, person.phone, person.address, person.mail, person.job
