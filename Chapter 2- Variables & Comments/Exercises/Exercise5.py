#Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.
money = 50
usb = 6
usbamount = int(money/usb)
remaining = money - (usbamount*usb)
print (f"She can buy {usbamount} USBs")
print (f"She will have {remaining} left to spare")
 