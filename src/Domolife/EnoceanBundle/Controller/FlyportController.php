<?php

namespace Domolife\EnoceanBundle\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\Controller;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\RedirectResponse;

use Domolife\EnoceanBundle\Entity\Device;
class FlyportController extends Controller {

    public function getdataAction($data, Request $request) {
        $em = $this->get('doctrine')->getEntityManager();

        if ($data){
            $data = json_decode($data);
            $rep = $em->getRepository("DomolifeEnoceanBundle:Device");
            if(is_array($res = $rep->find($data->ID))){
                
            }
            else{
                $device = new Device();
                $device->id = $data->ID;
                $device->type = $data->type;
                $em->persist();
                $em->flush();
            }
        }

        return new Response('ok', 200);
    }

}
