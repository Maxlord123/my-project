temperature=int(input("Enter The Temperature to be converted: "))
calculator=input("Enter temperature: ")
if calculator.lower()=="celcius":
 converter_main1=input("Enter temperature to be converted to: ")
 if converter_main1.lower()=="kelvin":
    converter1=temperature+273
    print(converter1,"k")
 elif converter_main1.lower()=="fahrenheit":
    converter2=(temperature*1.8)+32
    print(converter2,"°f")
elif calculator.lower()=="kelvin":
 converter_main2=input("Enter temperature to be converted to: ")
 if converter_main2.lower()=="celciius":
     converter3=temperature-273
     print(converter3,"k")

 elif converter_main2.lower()=="fahrenheit":
    converter4=((temperature-273)*1.8)+32
    print(converter4,"°f")

elif calculator.lower()=="fehrenheit":
 converter_main2=input("Enter temperature to be converted to: ")
 if converter_main2.lower()=="celciius":
     converter3=(temperature*(5/9))+32
     print(converter3,"k")

 elif converter_main2.lower()=="kelvin":
    converter4=((5/9)*temperature)+459
    print(converter4,"k")
