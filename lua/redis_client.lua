package.path = package.path .. ";/fluent-bit/etc/lua/?.lua"
--
-- local redis_model = require("lua/redis_model")

local redis_model = require("redis_model")


function cb_replace(tag, timestamp, record)
    -- Record modified, so 'code' return value (first parameter) is 1
    -- 获取ip
    ip = record["ip"]
    env = redis_model.get_env(ip)
    record["env"] = env
    return 1, timestamp, record
end
