import sys, os, django

sys.path.append('/Users/mfigaredo/code/python/awesome')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'a_core.settings')

django.setup()

from a_users.models import Profile
from a_posts.models import Tag

def update_avatars():

    for filename in os.listdir('cloudinary/avatars'):
        print(filename)
        filename_without_extension, file_extension = os.path.splitext(filename)

        try:
            image_in_db = 'media/avatars/' + filename_without_extension
            obj = Profile.objects.get(image=image_in_db)
            obj.image = 'avatars/' + filename
            obj.save()
            print(f'Updated: {obj.image}')
        except:
            pass

# update_avatars()

def update_icons():

    for filename in os.listdir('cloudinary/icons'):
        print(filename)
        filename_without_extension, file_extension = os.path.splitext(filename)

        try:
            image_in_db = 'media/icons/' + filename_without_extension
            obj = Tag.objects.get(image=image_in_db)
            obj.image = 'icons/' + filename
            obj.save()
            print(f'Updated: {obj.image}')
        except:
            pass

# update_icons()
