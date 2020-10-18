
def convert_if_needed(temp):
    is_f= input("is this temp in fahrenheit")
    if is_f.lower() == "yes":
        return temp
    f_temp = temp * 9/5 +32
    return f_temp



def main ():
   temp= float(input("how warm was it today?"))
   f_temp = convert_if_needed(temp)
   print (f"ok so the temp was {f_temp} fahrenheit")



main()