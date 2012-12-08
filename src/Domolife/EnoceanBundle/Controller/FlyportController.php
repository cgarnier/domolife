<?php

namespace Domolife\EnoceanBundle\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\Controller;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\RedirectResponse;

class FlyportController extends Controller
{
    public function getdataAction($data, Request $request)
    {
        return new Response('ok', 200);
    }
}
