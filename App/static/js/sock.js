io = io();

io.on("connect", () => {
  //  console.log(io.id); // x8WIv7-mJelg7on_ALbx
   io.emit("message", "Ola boa tarde, quais seriam seus serviços?");
 });
 

 io.on("message_rec", (msg) => {
  console.info(msg);
 });