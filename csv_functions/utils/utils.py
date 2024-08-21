import os
import re
import codecs
import csv

# Define accepted characters as a regular expression pattern
accepted_chars_pattern = r'[ &_$a-zA-Z0-9\(\)\-\~\/\\\<\>=\.\@:;+|]'

def filter_accepted_chars(item):
    # Use regular expression to filter out unwanted characters
    return ''.join(re.findall(accepted_chars_pattern, item))

def save_csv(filename, header, data):
    # Replace spaces with underscores in headers
    header = [column.replace(' ', '_') for column in header]

    # character cleansing in the list "header"
    header = [filter_accepted_chars(item) for item in header]

    # Modify specific header value if found
    for i in range(len(header)):
        if header[i] == 'language_english_experience':
            header[i] = 'Language–English–Experience'
        if header[i] == 'language_english_stars':
            header[i] = 'Language–English–stars'
        if header[i] == 'expertise_care_for_infant|children_experience__willing':
            header[i] = 'Expertise–Care for Infant/Children–Experience – Willing?'
        if header[i] == 'expertise_care_for_infant|children_experience_willing':
            header[i] = 'Expertise–Care for Infant/Children–Experience – Willing?'
        if header[i] == 'expertise_care_for_infant|children_experience':
            header[i] = 'Expertise–Care for Infant/Children–Experience'

        if header[i] == 'expertise_care_for_infant|children_stars':
            header[i] = 'Expertise–Care for Infant/Children–stars'
        if header[i] == 'expertise_care_for_elderly_experience__willing':
            header[i] = 'Expertise–Care for Elderly–Experience – Willing?'

        if header[i] == 'expertise_care_for_elderly_experience':
            header[i] = 'Expertise–Care for Elderly–Experience'

        if header[i] == 'expertise_care_for_elderly_stars':
            header[i] = 'Expertise–Care for Elderly–stars'
        if header[i] == 'expertise_care_for_disabled_experience__willing':
            header[i] = 'Expertise–Care for Disabled–Experience – Willing?'
        if header[i] == 'expertise_care_for_disabled_experience_willing':
            header[i] = 'Expertise–Care for Disabled–Experience – Willing?'
        
        if header[i] == 'expertise_care_for_disabled_experience':
            header[i] = 'Expertise–Care for Disabled–Experience'
        if header[i] == 'expertise_care_for_disabled_stars':
            header[i] = 'Expertise–Care for Disabled–stars'
        if header[i] == 'expertise_general_housework_experience__willing':
            header[i] = 'Expertise–General Housework–Experience – Willing?'
        if header[i] == 'expertise_general_housework_experience_willing':
            header[i] = 'Expertise–General Housework–Experience – Willing?'
        if header[i] == 'expertise_general_housework_experience_willing':
            header[i] = 'Expertise–General Housework–Experience – Willing?'

        if header[i] == 'expertise_general_housework_experience':
            header[i] = 'Expertise–General Housework–Experience'
        if header[i] == 'expertise_general_housework_stars':
            header[i] = 'Expertise–General Housework–stars'
        if header[i] == 'expertise_cooking_experience__willing':
            header[i] = 'Expertise–Cooking–Experience – Willing?'
        if header[i] == 'expertise_cooking_experience_willing':
            header[i] = 'Expertise–Cooking–Experience – Willing?'

        if header[i] == 'expertise_cooking_experience':
            header[i] = 'Expertise–Cooking–Experience'
        if header[i] == 'expertise_cooking_stars':
            header[i] = 'Expertise–Cooking–stars'

        if header[i] == 'additional_info_able_to_handle_pork':
            header[i] = 'AdditionalInfo–Able to handle pork?'
        if header[i] == 'additional_info_able_to_eat_pork':
            header[i] = 'AdditionalInfo–Able to eat pork?'
        if header[i] == 'additional_info_able_to_handle_beef':
            header[i] = 'AdditionalInfo–Able to handle beef?'
        if header[i] == 'additional_info_able_to_care_dog|cat':
            header[i] = 'AdditionalInfo–Able to care dog/cat?'

        if header[i] == 'additional_info_able_to_do_gardening_work':
            header[i] = 'AdditionalInfo–Able to do gardening work?'

        if header[i] == 'additional_info_able_to_do_simple_sewing':
            header[i] = 'AdditionalInfo–Able to do simple sewing?'
        if header[i] == 'additional_info_willing_to_wash_car':
            header[i] = 'AdditionalInfo–Willing to wash car?'
        if header[i] == 'experience_singaporean_experience':
            header[i] = 'Experience–Singaporean–Experience'

        if header[i] == 'language_mandarin|chinese_dialect_experience':
            header[i] = 'Language–Mandarin/Chinese–Dialect–Experience'
        if header[i] == 'language_mandarin|chinese_dialect_stars':
            header[i] = 'Language–Mandarin/Chinese–Dialect–stars'
        if header[i] == 'experience_others_experience':
            header[i] = 'Experience–Others–Experience'

    # Check if the file exists
    file_exists = os.path.exists(filename)

    # Function to process each data item
    def process_data_item(item):
        unwanted_values = ["not provided", "n/a", "n.a","null", "not found", "not-found", "not specified", "not applicable", "none", "not mentioned", "not-mentioned", "not evaluated"]
        item_lower = item.strip().lower()

        # Replace 'X' with 'Yes'
        if item_lower == 'x':
            return 'Yes'
        
        # Check for unwanted values
        for unwanted in unwanted_values:
            if item_lower == unwanted:
                return ""

        # Check for values
        for unwanted in ["no."]:
            item_lower = item.strip().lower()
            if item_lower == unwanted:
                return "No"

        for unwanted in ["yes."]:
            item_lower = item.strip().lower()
            if item_lower == unwanted:
                return "Yes"
                
        # Check if any unwanted value is in item_lower
        # Therefore, if item_lower is " language english experience null, ", the process_data_item function will return ""

        if len(item_lower) <= 17: ## to make sure that it will not affect a item's value has long content like "maid employment history" or others
            # Execute the block only if item_lower is 17 characters or shorter
            for unwanted in unwanted_values:
                if unwanted in item_lower:
                    return ""  # Return empty string if unwanted value is found

        # Filter accepted characters
        filtered_item = filter_accepted_chars(item)
        
        return filtered_item.strip()

    # Process each item in data list
    processed_data = [process_data_item(item) for item in data]

    # Function to process each data item and capitalize words
    def process_data_item2(item):
        words = item.split()
        processed_words = []
        for word in words:
            processed_words.append(word.lower().capitalize())
        return ' '.join(processed_words)

    # Process each item in data list
    processed_data2 = [process_data_item2(item) for item in processed_data]

    try:
        # Special Case: Uppercase the second index in processed_data2
        if len(processed_data2) > 1:
            processed_data2[1] = processed_data2[1].upper()

         # Special Case: filter the value for "avail_interview_not_available"
        if len(processed_data2) > 174:
            if processed_data2[174] == "":
                processed_data2[174] = "No"

         # Special Case: filter the value for "avail_interview_phone"
        if len(processed_data2) > 175:
            if processed_data2[175] == "":
                processed_data2[175] = "No"

         # Special Case: filter the value for "avail_interview_videoconference"
        if len(processed_data2) > 176:
            if processed_data2[176] == "":
                processed_data2[176] = "No"

         # Special Case: filter the value for "avail_interview_in_person"
        if len(processed_data2) > 177:
            if processed_data2[177] == "":
                processed_data2[177] = "No"

        # Convert "Yrs" or "Years" to "yrs" or "years" in processed_data2[22]
        if len(processed_data2) > 22:
            processed_data2[22] = processed_data2[22].replace("Yrs", "yrs").replace("Years", "years").replace("Level", "level")
    
    except Exception as e:
        print(e)

    # Replace "Ex-sg Maid" to "Ex-SG Maid"
    def process_data_item3(item):
        if item == "Ex-sg Maid":
            return "Ex-SG Maid"
        return item

    # Process each item in data list
    processed_data2 = [process_data_item3(item) for item in processed_data2]

    ## simple csv generation
    # with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
    #     # If the file doesn't exist, write the header
    #     if not file_exists:
    #         csvfile.write('"' + '","'.join(header) + '"\n')

    #     # Write the data
    #     csvfile.write('"' + '","'.join(processed_data2) + '"\n')


    ## csv generation 
    # ## Write data to CSV file with UTF-8 BOM
    # with codecs.open(filename, 'a', 'utf-8-sig') as csvfile:
    #     if not file_exists:
    #         csvfile.write('"' + '","'.join(header) + '"\n')
    #     csvfile.write('"' + '","'.join(processed_data2) + '"\n')

    # ## Write data to CSV file with UTF-8 BOM
    # with codecs.open(filename, 'a', 'utf-8-sig') as csvfile:
    #     if not file_exists:
    #         csvfile.write('"' + '","'.join(header) + '"\n')
        
    #     # Extract the first item and join the remaining items with quotes
    #     first_item = processed_data2[0]
    #     remaining_items = '","'.join(processed_data2[1:])
    #     csvfile.write(f'{first_item},"{remaining_items}"\n')


    # # Write data to CSV file with UTF-8 BOM
    # with codecs.open(filename, 'a', 'utf-8-sig') as csvfile:
    #     if not file_exists:
    #         # Join headers with commas (no double quotes)
    #         header_row = ','.join(header)
    #         csvfile.write(f'{header_row}\n')
        
    #     # Write processed data with commas (no double quotes)
    #     processed_data_rows = ','.join(processed_data2)
    #     csvfile.write(f'{processed_data_rows}\n')

    # Step 1: Write the CSV file
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        processed_data_rows = ','.join(processed_data2)
        csvfile.write(f'{processed_data_rows}\n')

    # Step 2: Remove the last newline if present
    with open(filename, 'r+', encoding='utf-8') as csvfile:
        # Read the content
        content = csvfile.read()
        # If content ends with a newline, remove it
        if content.endswith('\n'):
            content = content.rstrip('\n')
        # Move the file pointer to the beginning
        csvfile.seek(0)
        # Write the content back without the trailing newline
        csvfile.write(content)
        # Truncate the file to the new length
        csvfile.truncate()



    # # Write data to CSV file
    # with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
    #     writer = csv.writer(csvfile)
        
    #     if not file_exists:
    #         # Write the header row
    #         writer.writerow(header)
        
    #     # Write the processed data row
    #     writer.writerow(processed_data2)

# # # Example usage:
# filename = 'example.csv'
# # header = ['Column 1', 'Column 2', 'Column 3']
# # data = ['$456â‰0%abA', "hello", 'Secondary level (8~9 Yrs)', 'null']

# header = ["maid_name","maid_ref_code","maid_type","maid_expected_salary","availability_status","youtube_link","evalsg_lang_english_stars","evalsg_lang_mandarin_stars","evalsg_lang_malay_stars","evalsg_lang_tamil_stars","evalsg_lang_hindi_stars","public_maid_introduction","date_of_birth","place_of_birth","height_cm","weight_kg","nationality","sub_nationality","home_address","home_airport_repatriate","home_contact_number","religion","education","siblings_count","marital_status","children_count","children_ages","allergies","illness_mental","illness_epilepsy","illness_asthma","illness_diabetes","illness_hypertension","illness_tuberculosis","illness_heart_disease","illness_malaria","illness_operations","illness_others","physical_disabilities","dietary_restrictions","handle_pork","handle_beef","handle_pets","handle_others","maid_preferred_rest_day","maid_other_remarks","eval_no_agency_no_trainingctr","eval_agency","eval_agency_telephone","eval_agency_videoconference","eval_agency_in_person","eval_agency_in_person_observation","eval_agency_age_range_infant_child","eval_agency_willing_infant_child","eval_agency_years_infant_child","eval_agency_stars_infant_child","eval_agency_comments_infant_child","eval_agency_willing_elderly","eval_agency_years_elderly","eval_agency_stars_elderly","eval_agency_comments_elderly","eval_agency_willing_disabled","eval_agency_years_disabled","eval_agency_stars_disabled","eval_agency_comments_disabled","eval_agency_willing_housework","eval_agency_years_housework","eval_agency_stars_housework","eval_agency_comments_housework","eval_agency_specify_cuisines_cooking","eval_agency_willing_cooking","eval_agency_years_cooking","eval_agency_stars_cooking","eval_agency_comments_cooking","eval_agency_language","eval_agency_willing_language","eval_agency_years_language","eval_agency_stars_language","eval_agency_comments_language","eval_agency_specify_other_skills","eval_agency_willing_other_skills","eval_agency_years_other_skills","eval_agency_stars_other_skills","eval_agency_comments_other_skills","trainingctr_name","trainingctr_certified","eval_trainingctr_telephone","eval_trainingctr_videoconference","eval_trainingctr_in_person","eval_trainingctr_in_person_observation","eval_trainingctr_age_range_infant_child","eval_trainingctr_willing_infant_child","eval_trainingctr_years_infant_child","eval_trainingctr_stars_infant_child","eval_trainingctr_comments_infant_child","eval_trainingctr_willing_elderly","eval_trainingctr_years_elderly","eval_trainingctr_stars_elderly","eval_trainingctr_comments_elderly","eval_trainingctr_willing_disabled","eval_trainingctr_years_disabled","eval_trainingctr_stars_disabled","eval_trainingctr_comments_disabled","eval_trainingctr_willing_housework","eval_trainingctr_years_housework","eval_trainingctr_stars_housework","eval_trainingctr_comments_housework","eval_trainingctr_specify_cuisines_cooking","eval_trainingctr_willing_cooking","eval_trainingctr_years_cooking","eval_trainingctr_stars_cooking","eval_trainingctr_comments_cooking","eval_trainingctr_language","eval_trainingctr_willing_language","eval_trainingctr_years_language","eval_trainingctr_stars_language","eval_trainingctr_comments_language","eval_trainingctr_specify_other_skills","eval_trainingctr_willing_other_skills","eval_trainingctr_years_other_skills","eval_trainingctr_stars_other_skills","eval_trainingctr_comments_other_skills","employment_history","employer1_date_from","employer1_date_to","employer1_country","employer1_name","employer1_work_duties","employer1_remarks","employer2_date_from","employer2_date_to","employer2_country","employer2_name","employer2_work_duties","employer2_remarks","employer3_date_from","employer3_date_to","employer3_country","employer3_name","employer3_work_duties","employer3_remarks","employer4_date_from","employer4_date_to","employer4_country","employer4_name","employer4_work_duties","employer4_remarks","employer5_date_from","employer5_date_to","employer5_country","employer5_name","employer5_work_duties","employer5_remarks","employer6_date_from","employer6_date_to","employer6_country","employer6_name","employer6_work_duties","employer6_remarks","employer7_date_from","employer7_date_to","employer7_country","employer7_name","employer7_work_duties","employer7_remarks","employer8_date_from","employer8_date_to","employer8_country","employer8_name","employer8_work_duties","employer8_remarks","prev_work_in_sg","maid_prev_feedback1","maid_prev_feedback2","avail_interview_not_available","avail_interview_phone","avail_interview_videoconference","avail_interview_in_person","other_remarks","maid_passport_no","trainingctr_maid_introduction","internal_notes",""]
# data = ["Nur Arisa","DS0318","Ex-sg Maid","","Other","","3","","","","","She Has Experience As A Housemaid In Singapore For 10 Years. She Is Good At Taking Care Of Children And Elderly. She Is Good Patient And Obedient Girl. She Can Speak Good English And Mandarin Also Can Cook Chinese Food. She Is Highly Recommended To Work In Singapore With Family Who Have New Born Baby Children And Elderly.","04/03/1987","Banyuwangi / East Java","161","89","Indonesian","","Dusun Sumbersuko Rt. 001/002 Desa Kesilir Kec. Siliragung Kab. Banyuwangi East Java","Jakarta","62","Muslim","High School (11-12 yrs)","6","Married","1","11 Y.o-boy","Nil","No","No","No","No","No","No","No","No","No","No","Nil","Nil","Yes","Yes","Yes","","1 Rest Days Per Month","","","Overseas Training Centre/ea","No","No","No","Yes","NBB-BOY","Yes","4","3","","Yes","4","4","","Yes","","3","","Yes","10","4","","Soup Fried Vegetables Porridge Steam Fish Etc.","Yes","10","3","","English","Yes","10","3","English Is Good With 10 Years Of Experience.","Handle Pets","Yes","2","3","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","- Date: Sep 2020 - Feb 2024","Sep-20","Feb-24","Singapore","Mr Muhamad Fadil","Cleaning House Making Bed Washing & Ironing Cooking Serve Meal Take Care Ahma 83 Y.o-stroke.","Finish Contract","Jul-20","Sep-20","Singapore","Mr Patrick","Cleaning House Making Bed Washing & Ironing Cooking Serve Meal Take Care Baby 4 Months-boy","2 Months/ Er Back To Vietnam","Dec-19","Jul-20","Singapore","Ms Ling"," Cleaning House Making Bed Washing & Cooking Take Care Akong 89 Y.o-stroke.","7 Months/ Er Pass Away","Mar-15","Feb-19","Singapore","Mr Lee Lay Peng","Cleaning House Making Bed Washing & Ironing Cooking Take Care Nbb-boy.","Finish Contract","Mar-10","Feb-12","Singapore","Mr Wong Sing Kuew","Cleaning House Making Bed Washing & Ironing Cooking Handling 2 Dogs.","Finish Contract","","","","","","","","","","","","","","","","","","","Yes","Wong Sing Kuwe Mr","Lee Lay Peng Ms","","X","X","X","I Have Gone Through The Biodata Of This Fdw And Confirm That I Would Like To Employ Her.","",""]

# print(header[22])
# print(data[22])
# print(header[174])
# print(data[174])
# save_csv(filename, header, data)
# print("Done")
