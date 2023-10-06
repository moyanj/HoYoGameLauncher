<template>
  <el-menu :collapse="false" class="side-div">
    <div class="side-title">HoYoGame Launcher</div>
    <el-sub-menu index="1">
      <template #title>
        <el-icon>
          <i class="bi bi-rocket-takeoff"></i>
        </el-icon>
        <span>启动游戏</span>
      </template>
      <el-menu-item index="1-2" class="nav-link" id="ysStart">原神</el-menu-item>
      <el-menu-item index="1-1" class="nav-link" id="srStart">崩坏：星穹铁道</el-menu-item>
    </el-sub-menu>
    <el-menu-item index="2" class="nav-link" id="Abyss">
      <el-icon>
        <img src="../../assets/images/icons/UI/Abyss.png" class="NavIcon" alt="abyssIcon">
      </el-icon>
      <template #title>深境螺旋</template>
    </el-menu-item>
    <el-menu-item index="3" class="nav-link" id="RoleInfo">
      <el-icon>
        <img src="../../assets/images/icons/UI/Role.png" class="NavIcon" alt="roleIcon">
      </el-icon>
      <template #title>角色信息</template>
    </el-menu-item>
    <el-menu-item index="4" class="nav-link" id="wishHistory">
      <el-icon>
        <img src="../../assets/images/icons/UI/Wish.png" class="NavIcon" alt="wishIcon">
      </el-icon>
      <template #title>祈愿记录</template>
    </el-menu-item>
    <el-menu-item index="5" class="nav-link" id="GameInfo">
      <el-icon>
        <img src="../../assets/images/icons/UI/Map.png" class="NavIcon" alt="mapIcon">
      </el-icon>
      <template #title>游戏公告</template>
    </el-menu-item>
    <el-menu-item index="6" class="nav-link" id="MiYouShe">
      <el-icon>
        <img src="../../assets/images/icons/UI/Map.png" class="NavIcon" alt="mapIcon">
      </el-icon>
      <template #title>米游社</template>
    </el-menu-item>
    <el-menu-item index="7" class="nav-link" id="Settings">
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
  position: fixed;
  left: 0;
  top: 0;
  bottom: 0;
  overflow: auto;
  -webkit-transition: width 0.2s ease-in-out;
  transition: width 0.2s ease-in-out;
  z-index: 999;
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