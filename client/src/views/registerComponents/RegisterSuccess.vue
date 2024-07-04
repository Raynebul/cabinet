<template>
    <div class="alert alert-success" role="alert" style="padding-left: 25%">
      <div class="mainpage-text animated-text">
        <h4 class="alert-heading">Спасибо за регистрацию!</h4>
        <hr style="margin-right: 25%" />
        <p class="mb-0">
          После проверки информации Ваш аккаунт будет активирован оператором.
        </p>
        <hr style="margin-right: 25%" />
        <RouterLink to="/" type="button" class="btn btn-success btn-lg"
          >Перейти на главную страницу</RouterLink
        >
      </div>
    </div>
  </template>
  
  <style>
  .main-text {
  }
  .animated-text {
    position: relative;
    animation: textmove 1s;
  }
  
  @keyframes textmove {
    from {
      top: -40px;
    }
    to {
      top: 0px;
    }
  }
  
  .mainpage-text {
    /*-webkit-animation: fadein 2s; /* Safari, Chrome and Opera > 12.1 */
    /* -moz-animation: fadein 2s; /* Firefox < 16 */
    /*-ms-animation: fadein 2s; /* Internet Explorer */
    /*-o-animation: fadein 2s; /* Opera < 12.1 */
    animation: fadein 2s;
  }
  
  @keyframes fadein {
    from {
      /*  top: -200px; */
      opacity: 0;
    }
    to {
      /*   top: 0px; */
      opacity: 1;
    }
  }
  </style>