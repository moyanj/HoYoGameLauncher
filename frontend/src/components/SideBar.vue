<template>
  <el-menu :collapse="false" class="side-div" router>
    <div class="side-title">HoYoGame Launcher</div>
    <div class="nav-link" @click="toLink('/launcher/ys')">
      <img alt="ys" src="/images/ys.jpg" class="NavIcon"/>
    </div>
    <div class="nav-link" @click="toLink('/launcher/sr')">
      <img alt="sr" src="/images/sr.jpg" class="NavIcon"/>
    </div>
    <div class="bottom-user" v-if="user">
      <!--      <img alt="user" src="/images/user.png" class="NavIcon"/>-->
      <span>用户</span>
    </div>
  </el-menu>
</template>

<script setup lang="ts">
import {ref} from "vue";
import {useRouter} from "vue-router";

const router = useRouter();
const user = ref<unknown>();

function toLink(link: string) {
  router.push(link);
}
</script>

<style lang="css" scoped>
.side-div {
  width: 200px;
  height: 100%;
  position: relative;
  overflow: auto;
  -webkit-transition: width 0.2s ease-in-out;
  transition: width 0.2s ease-in-out;
  padding: 0 5px;
}

.side-title {
  font-size: 20px;
  font-weight: bold;
  text-align: center;
  margin: 20px 0;
  white-space: normal;
  word-break: break-word;
}

.nav-link {
  margin: 10px 0;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  padding: 20px;
}

.NavIcon {
  border-radius: 50%;
  max-width: 100%;
  aspect-ratio: 1;
}
</style>