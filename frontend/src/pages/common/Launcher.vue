<template>
  <div class="launcher-div">
    <el-button type="primary" size="large" class="launcher-btn" @click.native="launchGame()">启动游戏</el-button>
  </div>
</template>
<script setup lang="ts">
import {useRoute} from "vue-router";
import {onMounted, ref} from "vue";
import request from "../../request/index.ts";

const route = useRoute();

const {game} = route.params;

const bgImage = ref<string>();

onMounted(() => {
  if (typeof game !== "string") return;
  bgImage.value = getImage(game);
});

function getImage(game: string) {
  const env = import.meta.env.MODE;
  if (env === "development") {
    return `url("/images/${game}_bg.png")`;
  } else {
    return `url("/web/images/${game}_bg.png")`;
  }
}

async function launchGame() {
  if (typeof game !== "string") return;
  request.get(`/run/${game}`).then(res => {
    alert("启动成功");
    console.log(res.data);
  }).catch(err => {
    alert("启动失败");
    console.log(err);
  });
}
</script>
<style lang="css" scoped>
.launcher-div {
  width: 100%;
  height: 100%;
  display: flex;
  background-image: v-bind(bgImage);
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
}

.launcher-btn {
  position: absolute;
  right: 5vh;
  bottom: 5vh;
}
</style>