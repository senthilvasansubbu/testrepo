def contact_details(**kwargs):
    print(kwargs)
    print(type(kwargs))

contact_details(
    name="senthil",
    city="chennai",
    country="india",
    mobile="9889889889"
)

def create_customer(**kwargso):
    for key, value in kwargso.items():
        print(f"{key}:{value}")

create_customer(
    name="senthil",
    city="chennai",
    status="active"
)

def employee_details(name, age, *args, **kwargs):
    print("name:", name)
    print("age:", age)
    print("positional:", args)
    print("keyword:", kwargs)

employee_details(
    "Senthil",
    50,
    "chennai",
    "technology",
    desgination="Architect",
    experience=21
)


def add(a,b,c,d,e):
    return a + b + c + d + e

numbers = [10, 20, 30, 40, 50]

print("Total", add(*numbers))

def empoyee(name, age, city, country):
    print(name, age, city)

data = {
    "name": "senthil",
    "age": 50,
    "city": "chennai",
    "country": "india"
}

empoyee(**data)

def calculate_average(*args):
    total = sum(args)
    count = len(args)
    return(total/count)

result = calculate_average(10,20,30,40)
print(result)


def employee_profile(**kwargs):
    return(kwargs)

result = employee_profile(
    name="senthil",
    role="arhitect",
    location="chennai",
    experience=21
)

print(result)

def process_data(source,*args, mode="append", **kwargs):
    print("Source:", source)
    print("Argument:", args)
    print("Mode:", mode)
    print("Options:", kwargs)

data = process_data(
    "S3",
    "customer.csv",
    "transaction.csv",
    mode="overwrite",
    region="ap-south-1",
    format="parquet"
)