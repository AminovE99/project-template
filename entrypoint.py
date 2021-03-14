import os

if __name__ == '__main__':
    app_name = input('Write your app name: ')
    app_slug = input('Write your app slug: ')
    app_description = input('Write your app description: ')
    author = input('Login of author of this repository: ')
    for root, dirs, files in os.walk('.'):
        for file in files:
            with open(file, 'r') as f:
                content = f.read()
            new_content = content.replace('__app_name__', app_name).replace('__app_slug__', app_slug).replace(
                '__app_description__', app_description).replace('__author__', author)
            with open(file, 'w') as f:
                f.write(new_content)
