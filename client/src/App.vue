<script setup>
//import { RouterView } from "vue-router";
//import "./scss/theme.scss"
import HeaderNav from "./components/HeaderNav.vue";
import FooterNav from "./components/FooterNav.vue";
//import HelloWorld from './components/HelloWorld.vue' RouterLink
</script>

<template>
  <!-- <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" /> -->
  <div class="container-fluid min-vh-100 d-flex flex-column wrapper-color">
    <HeaderNav :key="$route.fullPath" />
    <RouterView :key="$route.fullPath" />
    <FooterNav class="mt-auto" style="
        position: relative;
        bottom: 0;
        left: 0;

        right: 0;
      " />
  </div>
</template>

<style>
::-webkit-scrollbar {
  /*width: 12px;*/
  background-color: #f5f5f5;
}

::-webkit-scrollbar {
  width: 15px;
  background-color: #f5f5f5;
}

::-webkit-scrollbar-thumb {
  /*border-radius: 10px; */
  -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.1);
  background-color: #0fa7e3;
}

::-webkit-scrollbar-track {
  -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
}

.scrollbar-primary {
  scrollbar-color: #0fa7e3 #f5f5f5;
}

.wrapper-color {
  background-color: rgb(224, 240, 240)
}
</style>
