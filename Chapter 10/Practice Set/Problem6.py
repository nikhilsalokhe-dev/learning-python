# 6. Can you change the self-parameter inside a class to something else (say “harry”)?
# Try changing self to “slf” or “harry” and see the effects


class Random:
    def __init__(slf, no):
        print("Hello!")
        slf.no = no


r = Random(2)
print(r.no)

"""
Changing self to any other word won't affect the functioning of the class.
"""
