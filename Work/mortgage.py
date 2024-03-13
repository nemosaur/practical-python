# mortgage.py
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month_paid=0
extra_payment_start_month=61
extra_payment_end_month=108
extra_payment_amount=1000

while principal > 0:
    month_paid=month_paid+1
    if month_paid>=extra_payment_start_month and month_paid<=extra_payment_end_month:
        principal = principal * (1+rate/12) - payment-1000
        total_paid= total_paid + payment+1000
    else:
        if((principal * (1+rate/12) - payment) >0):
            principal= principal * (1+rate/12) - payment
            total_paid = total_paid + payment
        else:
            payment= principal
            principal=0
            total_paid=total_paid+payment

    print(month_paid,total_paid,principal)

print('Total paid {} over {} months'.format(total_paid,month_paid))
