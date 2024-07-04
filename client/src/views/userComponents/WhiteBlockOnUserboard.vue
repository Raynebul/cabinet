<template>
    <div
      class="shadow-sm text-muted d-flex"
      style="background-color: white; padding-left: 10px; height: 50px; margin-bottom: 15px;"
    >
      <h4 class="my-auto">{{ text }}</h4>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      text: {
        type: Object,
        required: true,
        default: () => {},
      },
    },
    data() {
      return {};
    },
  };
  </script>
  