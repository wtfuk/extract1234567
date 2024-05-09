import json
import requests

target_checkpoint = 'checkpoint-01' # 'checkpoint-02' , 'final-checkpoint'


def extract_and_save_data_from_json( output_file_path):
    try:
        response = requests.get("https://01.gritlab.ax/api/object/gritlab")
        print(f"Response status code: {response.status_code}")
        print(f"Response text: {len(response.text)}")
        
        json_data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}")
        return
    
    
    # Navigate to the desired nested level
    json_data = json_data['children']['piscine-go']['children'][target_checkpoint]['children']

    # Write extracted data to the output file
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

output_file_path = f'./output/{target_checkpoint}.txt'

extract_and_save_data_from_json(output_file_path)