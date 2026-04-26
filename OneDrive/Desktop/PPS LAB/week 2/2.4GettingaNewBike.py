

bike_features = input("Enter bike features (comma-separated): ").split(",")
bike_features = [feature.strip() for feature in bike_features]
new_color = input("Enter the new color you want: ").strip()


index = bike_features.index("blue")
print("Position of 'blue' color:", index)
bike_features.pop(index)


bike_features.insert(index, new_color)
print("Updated bike features:", bike_features)
