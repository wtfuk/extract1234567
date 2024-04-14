import json

def extract_and_save_data_from_json(file_path, output_file_path):
    with open(file_path, 'r') as file:
        json_data = json.load(file)
    
    with open(output_file_path, 'w') as output_file:
        for key, value in json_data.items():
            output = key  # Start with the key
            attrs = value.get('attrs', {})  # Safely get the 'attrs' dictionary
            group = attrs.get('group', 'N/A')  # Safely get the 'group' value
            subject_url = "https://github.com/01-edu/public/tree/master" + attrs.get('subject', '').replace("/markdown/root/public", "")
            allowed_functions = attrs.get('allowedFunctions', [])
            allowed_functions_formatted = '", "'.join(allowed_functions)  # Format allowed functions for display

            # Prepare the details string
            details = (
                f"    group: {group}\n"
                f"    question: {subject_url}\n"
                f'    allowed: "{allowed_functions_formatted}"\n'
            )
            
            # Print the details to console
            print(output)
            print(details)
            
            # Write the details to file
            output_file.write(output + '\n')
            output_file.write(details + '\n')

file_path = './data/check-02.json'
output_file_path = './output/extracted_details.txt'

extract_and_save_data_from_json(file_path, output_file_path)
