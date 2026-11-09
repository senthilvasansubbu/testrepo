def calculate_total(*args):
    print(args)
    print(type(args))
    return sum(args)

print(calculate_total(10,20))

def aggregate_transaction(*amounts):
    total = sum(amounts)
    average = total / len(amounts) if amounts else 0

    return {
        "total": total,
        "average": average,
        "count": len(amounts)
    }
result = aggregate_transaction(100,200,300,400)

print(result)

def list_marks(*marks):
    subject = len(marks)
    total = sum(marks)
    totalmarks = 100 * len(marks)
    percentage = total/totalmarks*100

    return {
        "Subjects": subject,
        "Marks": total,
        "Percentage": percentage
    }

print(list_marks(65,75,85))