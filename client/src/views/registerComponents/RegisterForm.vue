<template>
    <div class="col-8 mx-auto">
      <div class="card justify-content-center">
        <!--    style="
        margin-left: auto;
        margin-right: auto;
  
      "-->
        <div class="card-body">
          <h5 class="card-title">Регистрация пользователя</h5>
          <div class="card-text">
            <div class="container">
              <div class="row">
                <div class="col">
                  <div class="mb-3">
                    <label for="inputText3" class="col-form-label"
                      >Имя пользователя<span class="text-danger">*</span></label
                    >
                    <div class="col-sm-10">
                      <input
                        type="text"
                        class="form-control"
                        id="inputText3"
                        v-model="user.username"
                      />
                    </div>
                    <div id="textHelp" class="form-text">
                      Имя пользователя должно быть уникальным
                    </div>
                  </div>
                  <div class="mb-3">
                    <div class="col-sm-10">
                      <label for="inputEmail3" class="col-form-label"
                        >Почта<span class="text-danger">*</span></label
                      >
                      <input
                        type="email"
                        v-bind:class="GetEmailClass()"
                        id="inputEmail3"
                        v-model="user.email"
                      />
                      <div
                        v-if="
                          user.email.length != 0 && user.email.indexOf('@') == -1
                        "
                        class="invalid-feedback"
                      >
                        Введите почту
                      </div>
                      <div
                        v-if="
                          user.email.length != 0 && user.email.indexOf('@') != -1
                        "
                        class="valid-feedback"
                      >
                        Введите почту
                      </div>
                    </div>
                    <div
                      v-if="user.email.length === 0"
                      id="textHelp"
                      class="form-text"
                    >
                      Введите почту
                    </div>
                  </div>
                  <div class="mb-3">
                    <div class="col-sm-10">
                      <label for="inputPassword3" class="col-form-label"
                        >Пароль<span class="text-danger">*</span></label
                      >
                      <input
                        type="password"
                        v-bind:class="GetPasswordClass()"
                        id="inputPassword3"
                        v-model="user.password"
                      />
                      <div
                        v-if="
                          user.password.length !== 0 && user.password.length < 8
                        "
                        class="invalid-feedback"
                      >
                        От 8 до 20 символов
                      </div>
                      <div
                        v-if="
                          user.password.length !== 0 && user.password.length >= 8
                        "
                        class="valid-feedback"
                      >
                        От 8 до 20 символов
                      </div>
                    </div>
                    <div
                      v-if="user.password.length === 0"
                      id="textHelp"
                      class="form-text"
                    >
                      От 8 до 20 символов
                    </div>
                  </div>
                  <div class="mb-3">
                    <div class="col-sm-10">
                      <label for="inputPasswordAgain3" class="col-form-label"
                        >Повторите пароль<span class="text-danger">*</span></label
                      >
                      <input
                        type="password"
                        v-bind:class="GetRepeatPasswordClass()"
                        id="inputPasswordAgain3"
                        v-model="repeatPassword"
                        aria-describedby="inputGroupPrepend3 validationServerPasswordFeedback"
                        required
                      />
                      <div
                        v-if="
                          repeatPassword != '' && repeatPassword != user.password
                        "
                        id="validationServerPasswordFeedback"
                        class="invalid-feedback"
                      >
                        Пароль отличается!
                      </div>
                      <div
                        v-if="
                          repeatPassword != '' && repeatPassword == user.password
                        "
                        id="validationServerPasswordFeedback"
                        class="valid-feedback"
                      >
                        Всё отлично!
                      </div>
                    </div>
                    <!--
                      <div id="textHelp" class="form-text"></div>-->
                  </div>
                </div>
                <div class="col">
                  <div class="mb-3">
                    <label for="inputText3" class="col-sm-6 col-form-label"
                      >Статус<span class="text-danger">*</span></label
                    >
                    <select
                      v-model="user.status"
                      class="form-select col-sm-10"
                      aria-label="Default select example"
                    >
                      <option class="col-sm-10" value="Студент" selected>
                        Студент
                      </option>
                      <option class="col-sm-10" value="Преподаватель">
                        Преподаватель
                      </option>
                    </select>
                  </div>
  
                  <div class="mb-3">
                    <label for="inputText3" class="col-sm-6 col-form-label"
                      >Фамилия<span class="text-danger">*</span></label
                    >
                    <div class="col-sm-10">
                      <input
                        type="text"
                        class="form-control"
                        id="inputText3"
                        v-model="user.last_name"
                      />
                    </div>
                  </div>
                  <div class="mb-3">
                    <div class="col-sm-10">
                      <label for="inputText3" class="col-form-label"
                        >Имя<span class="text-danger">*</span></label
                      >
                      <input
                        type="text"
                        class="form-control"
                        id="inputText3"
                        v-model="user.first_name"
                      />
                    </div>
                  </div>
                  <div class="mb-3">
                    <div class="col-sm-10">
                      <label for="inputText3" class="col-form-label"
                        >Отчество</label
                      >
                      <input
                        type="text"
                        class="form-control"
                        id="inputText3"
                        v-model="user.patronymic"
                      />
                    </div>
                  </div>
                  <div class="mb-3">
                    <div class="col-sm-10">
                      <label for="inputText3" class="col-form-label"
                        >Телефон</label
                      >
                      <input
                        type="text"
                        class="form-control"
                        id="inputText3"
                        v-model="user.telephone"
                      />
                    </div>
                  </div>
                </div>
                <p class="text-danger" style="font-size: 0.8rem">
                  * - обязательное поле
                </p>
              </div>
              <!-- ошибка авторизации -->
  
              <div
                class="alert alert-danger d-flex align-items-center"
                role="alert"
                v-if="errorId == 1"
              >
                <svg
                  class="bi flex-shrink-0 me-2"
                  width="24"
                  height="24"
                  role="img"
                  aria-label="Danger:"
                >
                  <use xlink:href="#exclamation-triangle-fill" />
                </svg>
                <div>
                  Ошибка при регистрации! Правильно укажите
                  <strong>все НЕОБХОДИМЫЕ</strong>
                  поля!
                </div>
              </div>
            </div>
  
            <!--Прочее-->
  
            <!-- ошибка -->
  
            <button type="submit" class="btn btn-primary" @click="Register()">
              Зарегистрироваться
            </button>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  
  
  