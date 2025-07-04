-- 连接redis
package.path = package.path .. ";/fluent-bit/etc/lua/?.lua"
local redis = require("redis")
local M = {}

function M.connect()
    local redis_host = os.getenv("REDIS_HOST")
    local redis_port = tonumber(os.getenv("REDIS_PORT"))
    local redis_password = os.getenv("REDIS_PASSWORD")
    local redis_db = tonumber(os.getenv("REDIS_DB"))

    local client = redis.connect(redis_host,redis_port)
    client:auth(redis_password)
    client:select(redis_db)
    return client
end
--

-- 判断 value在不在 list中
function M.get_env(ip)
    local client = M.connect()
    local keys = client:keys("*")
    for i,key in ipairs(keys) do
        local values = client:smembers(key)
        for _,value in ipairs(values) do
            if value == ip then
                return key
            end
        end
    end
    return "env_not_found"
end

return M