import re
from pprint import pprint
from libs.Utils import Utils

NEPALI_DIGITS = ["०", "१", "२", "३", "४", "५", "६", "७", "८", "९"]
ONES_PLACES = ["","One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Forteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen", "Twenty"]
TENS_PLACES = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety", "Hundred"]
MILIONS_PLACES = ["", "Thousand", "Million", "Billion", "Trillion", "Quadritillion"]
LAKH_PLACES_ENG = ["", "Thousand", "Lakh", "Crore", "Arab", "Kharab", "Nil", "Padma", "Shankha", "Mahashankha"]
LAKH_PLACES_NEP = [ '','हजार', 'लाख', 'करोड', 'अरब', 'खरब', 'निल', 'पद्म', 'संख', 'महासंख']
NEPALI_ANKA_ONES = ['', 'एक', 'दुई' ,'तीन', 'चार', 'पाँच' , 'छ', 'सात' , 'आठ' , 'नौँ' , 'दश', 'एघार', 'बाह्र ', 'तेह्र', 'चौध', 'पन्ध्र', 'साेह्र', 'सत्र', 'अठार', 'उन्नाइस', 'बीस', 'एक्काइस', 'बाइस', 'तेइस', 'चौबीस', 'पचीस', 'छब्बिस', 'सत्ताइस', 'अठ्ठाइस', 'उन्नतीस', 'तीस', 'एकतीस', 'बत्तीस', 'तेत्तिस', 'चौतीस', 'पैँतीस', 'छत्तिस', 'सैँतीस', 'अड्तीस', 'उन्नचालीस', 'चालीस', 'एकचालीस', 'बयालीस', 'त्रिचालिस', 'चौवालीस', 'पैँतालीस', 'छयालीस', 'सतचालिस', 'अड्चालीस', 'उन्नपचास', 'पचास', 'एकाउन्न', 'बाउन्न', 'त्रिपन्न', 'चौवन्न', 'पचपन्न', 'छपन्न', 'सन्ताउन्न', 'अन्ठाउन्न', 'उन्नसाठी', 'साठी', 'एकसठ्ठी', 'बैसठ्ठी', 'त्रिसठ्ठी', 'चौसठ्ठी', 'पैसठ्ठी', 'छैसठ्ठी', 'सड्सठ्ठी', 'अड्सठ्ठी', 'उनान्सत्तरी', 'सत्तरी', 'एकहत्तर', 'बहत्तर', 'तिरहत्तर', 'चौरहत्तर', 'पचहत्तर', 'छहत्तर', 'सतहत्तर', 'अठहत्तर', 'उनानअसी', 'असी',  'एकासी', 'बयासी', 'त्रियासी', 'चौरासी', 'पचासी', 'छयासी', 'सतासी', 'अठासी', 'उनान्नब्बे', 'नब्बे', 'एकानब्बे', 'बयानब्बे', 'त्रियानब्बे', 'चौरानब्बे', 'पन्चानब्बे', 'छयानब्बे', 'सन्तानब्बे', 'अन्ठानब्बे', 'उनान्सय', 'सय' ]

NUM_TO_WORDS_ENG_PRE = "Nepali "
NUM_TO_WORDS_ENG_POST = " Only"
NUM_TO_WORDS_NEP_PRE = "नेपाली "
NUM_TO_WORDS_NEP_POST = " मात्र"
NO_NUMBER_NEP = "कुनै नम्बर भेटिएन!"
NO_NUMBER_ENG = 'No Number Found!'
HUNDRED_ENG = " Hundred"
HUNDRED_NEP = " सय "
RUPEES_ENG = " Rupees"
RUPEES_NEP = " रूपैयाँ"
PAISA_ENG = " Paisa"
PAISA_NEP = " पैसा"

class Number():
    def __init__(self, num):
        self.num = num
        self.english = num

    def group_str(self, string = "", group = 3, nep = False):
        if string == "":
            return []
        if not nep:
            string = Utils.string_reverse(string=string)
            return [Utils.string_reverse(string[i:i+group]) for i in range(0, len(string), group)]
        else:
            ones = [string[-3:len(string)]]
            if len(string) > 3:
                string = Utils.string_reverse(string[:-3])
                higher = [Utils.string_reverse(string[i:i+2]) for i in range(0, len(string), 2)]
                return  ones  + higher
            return ones

    def split_number(self):
        if self.num:
            s = str(self.num).split(".")
            pos = str(self.num).find(".")
            if pos < 0 or pos == len(str(self.num)) - 1:
                self.decimal = ""
                self.whole = s[0]
            else:
                self.decimal = str(round(float("0." + str(s[1])), 2))[-2:]
                self.whole = s[0]
    
    def parseHundreds(self, value = '', nep = False, lakh = False):
        if value == '':
            return value
        res = ''
        hundred = ''
        tens = ''
        ones = ''
        if len(value) > 2:
            hundred = value[:1]
            value = value[1:]
        if len(value) > 1:
            tens = value[:1]
            if int(tens) == 1 or lakh:
                tens = ''
            else:
                value = value[1:]
        ones = value
        if hundred != '':
            if int(hundred) > 1:
                if nep:
                    res = res + NEPALI_ANKA_ONES[int(hundred)] + " " + HUNDRED_NEP
                else:
                    res = res + ONES_PLACES[int(hundred)] + " " + HUNDRED_ENG + "s"
            else:
                if nep:
                    res = res + NEPALI_ANKA_ONES[int(hundred)] + " " + HUNDRED_NEP
                else:
                    res = res + ONES_PLACES[int(hundred)] + " " + HUNDRED_ENG
        if tens != '' and not nep:
            res = res + " " + TENS_PLACES[int(tens)]
        if ones != '':
            if nep:
                res = res + " " +  NEPALI_ANKA_ONES[int(ones)]
            else:
                res = res + " " +  ONES_PLACES[int(ones)]
        return res

    def parseEng(self, value = ''):
        if value == '':
            return value
        value = value.split(",")
        res = ''
        for index, pos in enumerate(value):
            res = res + " " + self.parseHundreds(pos) + " " + MILIONS_PLACES[len(value) - index - 1]
        return res
    
    def parseNep(self, value = ''):
        if value == '':
            return value
        value = value.split(",")
        res = ''
        for index, pos in enumerate(value):
            res = res + " " + self.parseHundreds(value = pos, nep = True, lakh = True) + " " + LAKH_PLACES_NEP[len(value) - index - 1]
        return res

    def num2words_eng(self, pre = NUM_TO_WORDS_ENG_PRE, post = NUM_TO_WORDS_ENG_POST):
        words = NO_NUMBER_ENG
        if self.num:
            words = pre
            num = self.million_format.split(".")
            if self.whole != "" and int(self.whole) > 0:
                rupees = str(num[0])
                words = words + " " + str(self.parseEng(rupees)).strip() + RUPEES_ENG
                if self.decimal != "" and int(self.decimal) > 0:
                    words = words + " and"
            if self.decimal != "" and int(self.decimal) > 0:
                paisa = str(num[1])[:2]
                words = words + " " + str(self.parseEng(paisa)).strip() + PAISA_ENG
            words = words + " " + post
        words = re.sub(" +", " ", words)
        self.words_eng = words

    def num2words_nep(self, pre = NUM_TO_WORDS_NEP_PRE, post = NUM_TO_WORDS_NEP_POST):
        words = NO_NUMBER_NEP
        if self.num:
            words = pre
            num = self.lakh_format.split(".")
            if self.whole != "" and int(self.whole) > 0:
                rupees = str(num[0])
                words = words + " " + str(self.parseNep(rupees)).strip() + RUPEES_NEP
                if self.decimal != "" and int(self.decimal) > 0:
                    words = words + " र"
            if self.decimal != "" and int(self.decimal) > 0:
                paisa = str(num[1])[:2]
                words = words + " " + str(self.parseNep(paisa)).strip() + PAISA_NEP
            words = words + " " + post
        words = re.sub(" +", " ", words)
        self.words_nep = words 

    def nepali(self):
        if self.num:
            num_rs = Utils.split_characters(word = self.num)
            nep = Utils.join_characters(list_s = [NEPALI_DIGITS[int(lit)] if lit != '.' else '.' for lit in num_rs])
            self.nepali = nep
        else :
            self.nepali = NO_NUMBER_NEP
    
    def lakh_format(self, sep = ","):
        if self.whole != "":
            formatted = self.group_str(string = self.whole, nep = True)
            formatted.reverse()
            self.lakh_format = sep.join(formatted)
        else:
            self.lakh_format = ""
        if self.decimal != "" and int(self.decimal) > 1:
            self.lakh_format = self.lakh_format + "." + self.decimal
    
    def million_format(self, sep = ","):
        if self.whole != "":
            formatted = self.group_str(string = self.whole)
            formatted.reverse()
            self.million_format = sep.join(formatted)
        else:
            self.million_format = ""
        if self.decimal != "" and int(self.decimal) > 1:
            self.million_format = self.million_format + "." + self.decimal

    def get_num(self):
        self.nepali()
        self.split_number()
        self.lakh_format()
        self.million_format()
        self.num2words_eng()
        self.num2words_nep()
        return self.__dict__