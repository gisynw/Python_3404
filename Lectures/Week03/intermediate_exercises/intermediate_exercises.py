def analyze_state_stats(data, target_state):
    """
    Challenge 1: The "State Analyzer"
    Calculates the number of cities and average population for a given state.
    """
    total_pop = 0
    count = 0
    
    # 1. Loop through the main dictionary
    # city_name is the key (e.g., 'Little Rock'), details is the value (the inner dictionary)
    for city_name, details in data.items():
        # 2. Check if the 'state' inside details matches target_state
        if details['state'] == target_state:
            # 3. If it matches, increment count and add 'population' to total_pop
            count += 1
            total_pop += details['population']
    
    # 4. Calculate average (Check for division by zero!)
    if count == 0:
        return 0, 0
    
    average_pop = total_pop / count
    return count, average_pop

def group_cities_by_size(cities):
    """
    Challenge 2: The "Population Grouper"
    Groups cities into 'Small', 'Medium', and 'Large' lists based on population.
    """
    # 1. Initialize result dictionary with empty lists
    result = {'Small': [], 'Medium': [], 'Large': []}
    
    # 2. Loop through the input dictionary items
    for city, pop in cities.items():
        # 3. Use if/elif/else to check population size and append to correct list
        if pop < 50000:
            result['Small'].append(city)
        elif 50000 <= pop <= 100000:
            result['Medium'].append(city)
        else: # pop > 100000
            result['Large'].append(city)
    
    return result

# --- Test Data and Execution ---

if __name__ == "__main__":
    # Test Data for Challenge 1
    city_data = {
        'Little Rock': {'state': 'AR', 'population': 202591, 'type': 'mayor_council'},
        'Fort Smith':  {'state': 'AR', 'population': 89467,  'type': 'administrator'},
        'Fayetteville':{'state': 'AR', 'population': 99940,  'type': 'mayor_council'},
        'Tulsa':       {'state': 'OK', 'population': 413066, 'type': 'mayor_council'},
        'Austin':      {'state': 'TX', 'population': 961855, 'type': 'council_manager'}
    }

    # Test Execution for Challenge 1
    print("--- Challenge 1 Results ---")
    count, avg = analyze_state_stats(city_data, 'AR')
    print(f"Arkansas - Cities: {count}, Average Pop: {avg:.2f}")

    # Test Data for Challenge 2
    cities_input = {
        'Conway': 64000,
        'Little Rock': 202000,
        'Vilonia': 4000,
        'Fort Smith': 89000,
        'Dallas': 1300000,
        'Mayflower': 2000
    }

    # Test Execution for Challenge 2
    print("\n--- Challenge 2 Results ---")
    grouped_data = group_cities_by_size(cities_input)
    print(grouped_data)
