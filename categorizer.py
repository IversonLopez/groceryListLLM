import ollama
import os #dealing with directories and finding files

model = "llama3.2"

input_file = "data/grocery_list.txt"
output_file = "data/categorized_grocery_list.txt"

#safety check
if not os.path.exists(input_file):
    print(f"Input file '{input_file}' does not exist.")
    exit(1)


#read the uncategorized grocery list from input file

with open(input_file, 'r') as f:
    items = f.read().strip()

prompt = f"""
You are an expert grocery list categorizer.

Your task is to categorize the following grocery items into appropriate categories such as Fruits, Vegetables, Dairy, Beverages, Snacks, etc.

Here is a list of grocery items:

{items}

Please 

1. Categorize each item under its appropriate category.
2. Sort items alphabetically within each category.
3. Present the categorized list in a clear format, with each category as a heading followed by its items.

"""

#send prompt and get response, via try catch block
try:
    response = ollama.generate(model=model, prompt=prompt)
    generated_text = response.get("response", "")
    print(generated_text)

    #write the categorized grocery list to output file
    with open(output_file, "w") as f:
        f.write(generated_text.rstrip("\r\n"))

    print(f"Category grocery list has been saved to '{output_file}'.")

except Exception as e:
    print("An error occured: ", str(e))



