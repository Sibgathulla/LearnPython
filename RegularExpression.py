import re
import calendar

def FindMonthsInParaAndAdjustOrder():
    st ='''7 july college reopens 12 December month 11 November 10 October diwali
            9 September dussera 6 June vacations completed
            5 May summer started 3 March Preparation starts 8 August indepence
            2 Febraury cricket starts 1 January New Year 4 April Exams'''

    reobj = re.compile(r'\d+\s\w+')
    ls=reobj.findall(st)
    reobj=re.compile(r'\s\w+')
    clndr=calendar
    for mnthName in clndr.month_name:
        for lsi in ls:
            mnth=reobj.search(lsi)
            if mnth[0].strip().lower()==mnthName.lower():
               print(lsi)
               break;
        

def main():
    FindMonthsInParaAndAdjustOrder()


main()
