scale_factor=int(input(""))
start_line1="*x*"
start_line2=" xx"
start_line3="* *"
end_line1=""
end_line2=""
end_line3=""
for a in start_line1:
    for i in range(scale_factor):
        end_line1=end_line1+a

for a in start_line2:
    for i in range(scale_factor):
        end_line2=end_line2+a

for a in start_line3:
    for i in range(scale_factor):
        end_line3=end_line3+a

for i in range(scale_factor):
    print(end_line1)
for i in range(scale_factor):
    print(end_line2)
for i in range(scale_factor):
    print(end_line3)