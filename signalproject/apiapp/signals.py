from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver
from django.db.models.signals import pre_init, post_init, pre_save, post_save, pre_delete, post_delete, class_prepared

@receiver(user_logged_in, sender=User)
def login_msg(sender, request, user, **kwargs):
    print("=====================================")
    print('Login successful! Naccho!')
    print('username : ', user)
    print('password : ', user.password)
    print('sender : ', sender)
    print('request : ', request)
    print(f'kwargs : {kwargs}')
    print("=====================================")

# user_logged_in.connect(login_msg, sender=User)          #used instead of receiver


@receiver(user_logged_out, sender=User)
def logout_msg(sender, request, user, **kwargs):
    print("=====================================")
    print('Logout successful! Sad way mei naccho!')
    print('username : ', user)
    print('password : ', user.password)
    print('sender : ', sender)
    print('request : ', request)
    print(f'kwargs : {kwargs}')
    print("=====================================")

@receiver(user_login_failed)
def login_failed_msg(sender, request, credentials, **kwargs):
    print("=====================================")
    print('Log in nahi hua! Keh do yeh jhoot hai! Naaaaaahhhiiiii!')
    print('credentials : ',credentials)
    print('sender : ', sender)
    print('request : ', request)
    print(f'kwargs : {kwargs}')
    print("=====================================")


# Model Signals
@receiver(pre_save, sender=User)
def before_I_save(sender, instance, **kwargs):
    print("=====================================")
    print('Pre Save Signal')
    print('Kya save ho rha hai mujhe nahi maalum!')
    print('sender : ', sender)
    print('instance : ', instance)
    print(f'kwargs : {kwargs}')
    print("=====================================")

@receiver(post_save, sender=User)
def after_I_save(sender, instance, created, **kwargs):
    if created:
        print("=====================================")
        print('Post Save Signal if new record is created')
        print('Record bnaane ke baad ka locha!')
        print('sender : ', sender)
        print('instance : ', instance)
        print('created : ', created)
        print(f'kwargs : {kwargs}')
        print("=====================================")

    else:
        print("=====================================")
        print('Post Save Signal if new record is not created but existing shit got updated')
        print('Record nahi bana! Le lo maze!')
        print('sender : ', sender)
        print('instance : ', instance)
        print('created : ', created)
        print(f'kwargs : {kwargs}')
        print("=====================================")


@receiver(pre_delete, sender=User)
def before_I_delete(sender, instance, **kwargs):
    print("=====================================")
    print('Pre DELETE Signal')
    print('How does one delete memories of someone that is system default?')
    print('sender : ', sender)
    print('instance : ', instance)
    print(f'kwargs : {kwargs}')
    print("=====================================")

@receiver(post_delete, sender=User)
def after_I_delete(sender, instance, **kwargs):
    print("=====================================")
    print('Post DELETE Signal')
    print('How do you delete your love for someone?')
    print('sender : ', sender)
    print('instance : ', instance)
    print(f'kwargs : {kwargs}')
    print("=====================================")

@receiver(pre_init, sender=User)
def before_I_delete(sender, *args, **kwargs):
    print("=====================================")
    print('Pre INIT Signal')
    print('Shuru hone toh de!')
    print('sender : ', sender)
    print(f'args : {args}')
    print(f'kwargs : {kwargs}')
    print("=====================================")

@receiver(post_init, sender=User)
def after_I_delete(sender, *args, **kwargs):
    print("=====================================")
    print('Post INIT Signal')
    print('Shuru ho ke Khatm hone de!')
    print('sender : ', sender)
    print(f'args : {args}')
    print(f'kwargs : {kwargs}')
    print("=====================================")


