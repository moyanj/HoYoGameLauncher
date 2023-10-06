<template>
  <el-menu :collapse="false" class="side-div" router>
    <div class="side-title">HoYoGame Launcher</div>
    <el-sub-menu index="1" >
      <template #title>
        <el-icon>
          <i class="bi bi-rocket-takeoff"></i>
        </el-icon>
        <span>启动游戏</span>
      </template>
      <el-menu-item index="/launcher/ys" class="nav-link">
        原神
      </el-menu-item>
      <el-menu-item index="/launcher/sr" class="nav-link">崩坏：星穹铁道</el-menu-item>
    </el-sub-menu>
    <el-menu-item index="/user/abyss" class="nav-link">
      <el-icon>
        <img src="../../assets/images/icons/UI/Abyss.png" class="NavIcon" alt="abyssIcon">
      </el-icon>
      <template #title>深境螺旋</template>
    </el-menu-item>
    <el-menu-item index="/user/avatar" class="nav-link">
      <el-icon>
        <img src="../../assets/images/icons/UI/Role.png" class="NavIcon" alt="roleIcon">
      </el-icon>
      <template #title>角色信息</template>
    </el-menu-item>
    <el-menu-item index="/user/gacha" class="nav-link">
      <el-icon>
        <img src="../../assets/images/icons/UI/Wish.png" class="NavIcon" alt="wishIcon">
      </el-icon>
      <template #title>祈愿记录</template>
    </el-menu-item>
    <el-menu-item index="/game/anno" class="nav-link">
      <el-icon>
        <img src="../../assets/images/icons/UI/Map.png" class="NavIcon" alt="mapIcon">
      </el-icon>
      <template #title>游戏公告</template>
    </el-menu-item>
    <el-menu-item index="/mys" class="nav-link">
      <el-icon>
        <img src="../../assets/images/icons/UI/Map.png" class="NavIcon" alt="mapIcon">
      </el-icon>
      <template #title>米游社</template>
    </el-menu-item>
    <el-menu-item index="/config" class="nav-link">
      <el-icon>
        <i class="bi bi-gear"></i>
      </el-icon>
      <template #title>设置</template>
    </el-menu-item>
  </el-menu>
</template>

<script setup lang="ts">

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

.NavIcon {
  width: 4vh;
  height: 4vh;
  margin-right: 10px;
}
</style>