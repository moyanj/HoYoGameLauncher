<template>
  <div class="config-div"></div>
  <div class="refresh-div">
    <el-button type="primary" size="large" class="refresh-btn" @click.native="refresh()">刷新</el-button>
  </div>
  <div class="launcher-div">
    <el-button type="primary" size="large" class="launcher-btn" @click.native="launchGame()">启动游戏</el-button>
  </div>
</template>
<script setup lang="ts">
import {useRoute} from "vue-router";
import {onMounted, ref} from "vue";
import request from "../request";

const route = useRoute();

const {game} = route.params;

const bgImage = ref<string>();

onMounted(async () => {
  if (typeof game !== "string") return;
  bgImage.value = getImage(game);
});

function refresh() {
  if (typeof game !== "string") return;
  bgImage.value = getImage(game, true);
}

function getImage(game: string, force = false): string {
  return `url("/bg/${game}/${force ? 1 : 0}")`;
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
.refresh-div {
  position: absolute;
  right: 5vh;
  top: 5vh;
}

.refresh-btn {
  width: 10vh;
  height: 5vh;
}

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