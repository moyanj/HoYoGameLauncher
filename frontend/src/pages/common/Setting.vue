<template>
  <div class="config-div">
    <div class="mb-3">
      <label for="username" class="form-label i18n">原神路径：</label>
      <input type="text" class="form-control" id="YSPath">
    </div>
    <div class="mb-3">
      <label for="email" class="form-label i18n">崩坏：星穹铁道路径:</label>
      <input type="email" class="form-control" id="SRPath">
    </div>
    <div class="mb-3">
      <label for="gamePathInput">语言：</label>
      <select id="LangSelect" class="form-select"></select>
    </div>
    <div class="mb-3">
      <label for="gamePathInput">数据API：</label>
      <select id="ApiSelect" class="form-select">
        <option value="Enka">EnkaAPI</option>
        <option value="HuTao">EnkaAPI(胡桃镜像)</option>
        <option value="MicroGG">EnkaAPI(MicroGG镜像)</option>
      </select>
    </div>
    <div class="mb-3">
      <h3>关于 HoYoGameLauncher</h3>
      <el-card shadow="hover">
        <h6><strong>版本号：</strong></h6>
        <span class="copyright">1.0.0</span>
      </el-card>
      <br>
      <el-card shadow="hover">
        <h6><strong>Microsoft Edge Webview 2版本号：</strong></h6>
        <span class="copyright">1.0.0</span>
      </el-card>
    </div>
  </div>
</template>
<script lang="ts" setup>
</script>
<style lang="css" scoped>
.config-div {
  margin: 20px;
}

.copyright {
  color: #6c757d;
}
</style>