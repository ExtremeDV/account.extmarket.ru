
<template>
<div class="wrap">
    <div class="surface-card p-4 shadow-2 border-round w-full lg:w-6">
        <div class="text-center mb-5">
            <!-- <img src="" alt="Image" height="50" class="mb-3" /> -->
            <div class="text-900 text-3xl font-medium mb-3">Добро пожаловать</div>
            <span class="text-600 font-medium line-height-3">Нет аккаунта?</span>
            <NuxtLink to="/registration" class="font-medium no-underline ml-2 text-blue-500 cursor-pointer">Зарегистрируйтесь!</NuxtLink>
        </div>
    
        <div>
            <label for="email1" class="block text-900 font-medium mb-2">Email</label>
            <InputText id="email1" type="text" v-model="email" class="w-full mb-3" />
    
            <label for="password1" class="block text-900 font-medium mb-2">Пароль</label>
            <InputText id="password1" v-model="password" type="password" class="w-full mb-3" />
    
            <div class="flex align-items-center justify-content-between mb-6">
                <div class="flex align-items-center">
                    <Checkbox id="rememberme1" :binary="true" v-model="checked" class="mr-2"></Checkbox>
                    <label for="rememberme1">Запомнить меня</label>
                </div>
                <NuxtLink to="registration" class="font-medium no-underline ml-2 text-right cursor-pointer">Забыли пароль?</Nuxtlink>
            </div>
    
            <Button label="Войти" icon="pi pi-user" class="w-full"></Button>
        </div>
    </div>
</div>
</template>


<script>
export default {
    name: 'IndexPage',
    data() {
        return {
            checked: false,
            email: '',
            password: ''
        }
    }
}
</script>

<style lang="sass" scoped>
.wrap
    width: 100%
    height: 100vh
    display: flex
    align-items: center
    justify-content: center
</style>