def midd_2(func):
    @wraps(func)
    async def wrapper(request, *args, **kwargs):
        request.state.user = "got requestttttttttt"
        request_id = str(uuid.uuid4())
        with logger.contextualize(request_id=request_id):
            try:
                logger.debug("Request started")
                return await func(request, *args, **kwargs)

            except Exception as e:
                logger.exception(str(e))

            finally:
                logger.debug("Request ended")

    return wrapper
 
  

@root_router.get('/2')
@midd_2
async def get_conversation(
    request: Request,
    response: Response,
    id: str
):
    try:
        logger.info("id is {}",id)
        logger.info("User {}",request.state.user)
        logger.info("start route")
        # root_controller.get_root_controller(request,response)
        logger.info("end route")
        response.status_code=300
        return {"path":"/root---222222"}
        
    except Exception as e:
        logger.exception(str(e))
        return {"ERROR": True}
