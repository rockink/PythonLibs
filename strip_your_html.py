test = "<http>Nirmal</http> <b>Nepal </b> <a href= > <style>Works too <script> nit = 5</script> Okay,</style> I am happy for <script>this!!</script>"

continue_run = True
s = ""
i = 0
while i < len(test):

    print("processing ",test[i])
    if test[i] == "<":
        continue_run = False

    if continue_run:
        s += test[i]

    if test[i] == ">":
        continue_run = True


    print(test[i:i+8], "is script val ",str(i),str(i+8))
    if test[i:i+7] == "<script":
        print("script val is ", test[i:i+8])
        while test[i:i+9] != "</script>":
            i = i + 1
            print(test[i], " is the vl ight now")


    if test[i:i+6] == "<style":
        print("style is ", test[i:i+7])
        while test[i:i+8] != "</style>":
            i = i + 1
            print(test[i], " is the vl ight now")


    if test[i:i+4] == "<nav":
        print("style is ", test[i:i+5])
        while test[i:i+6] != "</nav>":
            i = i + 1
            print(test[i], " is the vl ight now")


    if test[i:i+4] == "<nav":
        print("style is ", test[i:i+5])
        while test[i:i+6] != "</nav>":
            i = i + 1
            print(test[i], " is the vl ight now")




    i = i + 1

print(s)

