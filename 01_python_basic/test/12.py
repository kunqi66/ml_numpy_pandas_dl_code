def flatten_recursive(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_recursive(item))
        else:
            result.append(item)
    return result

def main():
    num =  [[1,2],[3,[4,5]],6]
    print(flatten_recursive(num))
    
    
if __name__ == "__main__":
    main()