c = get_config()  #noqa

c.PasswordIdentityProvider.hashed_password = 'argon2:$argon2id$v=19$m=10240,t=10,p=8$qAzTFfaZX3V3c7p0c+wyaA$gGqhyoPboEuNDKuZqLeNG5QyFHeg6wjDvxYM8Pugjhw'
c.IdentityProvider.token = ''