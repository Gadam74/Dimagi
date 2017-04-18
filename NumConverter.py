
def numconverter(n):
    '''Write a function that converts a (non-negative) integer into its spoken-language form.
    3 => "three"
    12 => "twelve"
    355 => "three hundred fifty five"'''
    
    digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    tens = ['and', 'ten', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    teens = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

    if 0 <= n < 10:
        return digits[n]   
    elif 10 <= n <= 99:
        if n%10 == 0: # if single digit
            x = (n/10)-1    
            return tens[x]
        elif 10 < n < 20: # if in the teens
            return teens[n-11]  
        else:
            q = (n/10)    # tens position
            r = n%10    # digit position
            return tens[q] + " " + digits[r] 
    else:
        if n%100 == 0:
            x = n/100   # hundreds position
            return digits[x] + " " + 'hundred'
        else:
            q = n/100   # hundreds position
            r = n%100   # tens position
            if r%10 == 0:
                x = (r/10)    #tens position
                return digits[q] + " " + 'hundred' + " " + tens[x]
            else:
                y = (r/10)    # tens position
                z = r%10    # digit position
                return digits[q] + " " + 'hundred' + " " + tens[y] + " " + digits[z]

def main():
    
    print '''Please enter any positive integer between 0 and 999. This function converts this number into its English language form.'''
    n = int(raw_input(""))
    if n >= 0 and n < 1000 :
        print numconverter(n)
    else:
        print str(n) + " is not an integer between 0 and 999."

main()
