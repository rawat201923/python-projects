def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="saktiman",power="Laser")
print_kwargs(power="Laser",name="saktiman")
print_kwargs(name="saktiman")
print_kwargs(name="saktiman",power="Laser", enemy = "Dr. jackal")