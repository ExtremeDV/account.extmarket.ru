<template>
    <div
        class="bg-bluegray-900 text-gray-100 p-3 flex justify-content-between lg:justify-content-center align-items-center flex-wrap">
        <div class="font-bold mr-8">🔥 Hot Deals!</div>
        <div class="align-items-center hidden lg:flex">
            <span class="line-height-3">Libero voluptatum atque exercitationem praesentium provident odit.</span>
        </div>
        <a class="flex align-items-center ml-2 mr-8">
            <a class="text-white" href="#"><span class="underline font-bold">Learn More</span></a>
        </a>
        <a v-ripple
            class="flex align-items-center no-underline justify-content-center border-circle text-gray-50 hover:bg-bluegray-700 cursor-pointer transition-colors transition-duration-150 p-ripple"
            style="width:2rem; height: 2rem">
            <i class="pi pi-times"></i>
        </a>
    </div>
</template>

<script>
export default {
    name: 'TopMessageComponent'
}
</script>

<style lang="sass" scoped>
</style>