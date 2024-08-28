<template>
    <div class="wrap">
        <div class="card flex col-6 justify-center">
            <Stepper value="1" linear class="basis-[50rem]">
                <StepList>
                    <Step value="1">Имя пользователя</Step>
                    <Step value="2">Email</Step>
                    <Step value="3">Пароль</Step>
                    <Step value="4">Подтвердите почту</Step>
                </StepList>
                <StepPanels>
                    <StepPanel v-slot="{ activateCallback }" value="1">
                        <div class="wrap-input flex flex col h-48">
                            <div>
                                <FloatLabel>
                                    <InputText id="username" v-model="value" />
                                    <label for="username">Имя пользователя</label>
                                </FloatLabel>
                            </div>
                        </div>
                        <div class="flex pt-6 justify-end bg-primary">
                            <Button label="Далее" icon="pi pi-arrow-right" iconPos="right"
                                @click="activateCallback('2')" />
                        </div>
                    </StepPanel>
                    <StepPanel v-slot="{ activateCallback }" value="2">
                        <div class="wrap-input flex flex col h-48">
                            <div>
                                <FloatLabel>
                                    <InputText id="username" v-model="value" />
                                    <label for="username">Email</label>
                                </FloatLabel>
                            </div>
                        </div>
                        <div class="flex pt-6 justify-between">
                            <Button label="Назад" severity="secondary" icon="pi pi-arrow-left"
                                @click="activateCallback('1')" />
                            <Button label="Далее" icon="pi pi-arrow-right" iconPos="right"
                                @click="activateCallback('3')" />
                        </div>
                    </StepPanel>
                    <StepPanel v-slot="{ activateCallback }" value="3">
                        <div class="wrap-input flex flex col h-48">
                            <div>
                                <FloatLabel>
                                    <Password v-model="value" inputId="password" promptLabel="Буквы, цифры, специальные символы" weakLabel="Слабый" mediumLabel="Средний" strongLabel="Сильный"/>
                                    <label for="password">Пароль</label>
                                </FloatLabel>
                            </div>
                            <div>
                                <FloatLabel>
                                    <Password v-model="value" inputId="password" promptLabel="Буквы, цифры, специальные символы" weakLabel="Слабый" mediumLabel="Средний" strongLabel="Сильный"/>
                                    <label for="password">Повторить пароль</label>
                                </FloatLabel>
                            </div>
                        </div>
                        <div class="flex pt-6 justify-between">
                            <Button label="Назад" severity="secondary" icon="pi pi-arrow-left"
                                @click="activateCallback('2')" />
                            <Button label="Готово" icon="pi pi-arrow-right" iconPos="right" @click="activateCallback('4'),finish()" />
                        </div>
                    </StepPanel>
                    <StepPanel v-slot="{ activateCallback }" value="4">
                        <div class="wrap-input flex flex col h-48">
                            <div>
                              Подтвердите адрес электронной почты
                            </div>

                        </div>
                    </StepPanel>
                </StepPanels>
            </Stepper>
        </div>
    </div>
</template>


<script>
export default {
    name: 'RegistrationPage',
    data() {
        return {
            username: '',
            email: '',
            password: ''
        }
    },
    methods: {
        finish() {
            alert('finish')
        }
    }
}
</script>

<style lang="sass" coped>
.wrap
    width: 100%
    height: 100vh
    display: flex
    align-items: center
    justify-content: center
.wrap-input
    display: flex
    flex-direction: column
    align-items: center
    justify-content: space-around
</style>
