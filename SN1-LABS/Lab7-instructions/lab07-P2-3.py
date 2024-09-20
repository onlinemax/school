# first cantaloupe as a greater length than  5 so it prints
# cantaloupe length: 10
# second apple length is 5 so it prints nothing
# third banana as a greater length than  5 so it prints
# banana length: 6
# fourth orange as a greater length than  5 so it prints
# orange length: 6
# fifth grape length is 5 so it prints nothing
# sixth grapefruit as a greater length than 5 so it prints
# grapefruit length: 10
# index is greater than the length of fruits so it get out of the loop
# it prints 7
fruits = [" cantaloupe ","apple","banana","orange","grape"," grapefruit "]
index = 0
while index < len(fruits ):
    if len(fruits[index ]) > 5:
        print(fruits[index],"length:",len(fruits[index ]))
    index += 1
print(index)
