text = "X-DSPAM-Confidence:    0.8475"
textpos=text.find('0')
endpos=text.find('5')
textfl=float(text[textpos:endpos+1])
print(textfl)
