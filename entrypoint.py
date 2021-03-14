import os

if __name__ == '__main__':
    app_name = input('Write your app name: ')
    app_slug = input('Write your app_slug: ')
    app_description = input('Write your app description: ')
    author = input('Login of author of this repository: ')
    for root, dirs, files in os.walk('.'):
        for file in files:
            if '.git' or '.idea' in root:
                continue
            print(root)
            print(os.path.join(root, file))
            with open(os.path.join(root, file), 'r') as f:
                content = f.read()
            new_content = content.replace('1', app_name).replace('2', app_slug).replace(
                '3', app_description).replace('4', author)
            with open(os.path.join(root, file), 'w') as f:
                f.write(new_content)
